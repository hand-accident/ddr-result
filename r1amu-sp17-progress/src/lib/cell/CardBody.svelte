<script>
    let className;
    export { className as class };
</script>

<div class="c {className}">
    <slot />
</div>

<style lang="postcss" module>
    .c {
        padding: var(--padding-card, 2rem);
        @apply flex flex-auto flex-col gap-2;
    }
</style>
