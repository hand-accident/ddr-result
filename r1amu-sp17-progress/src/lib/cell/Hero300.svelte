<script>
    let className;
    export { className as class };
</script>

<div class="a {className}">
    <slot />
</div>

<style lang="postcss" module>
    .a {
        @apply hero bg-base-300;
    }
</style>
